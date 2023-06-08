import {SubmitHandler, useForm} from 'react-hook-form';
import {yupResolver} from '@hookform/resolvers/yup';
import * as yup from 'yup';
import {useSession} from "next-auth/react";

type Inputs = {
    currentPassword: string;
    newPassword: string;
    confirmPassword: string;
};

const schema = yup.object({
    currentPassword: yup.string().required('Old password is required'),
    newPassword: yup.string().required('New password is required').min(8, 'Password must be at least 8 characters').max(50, 'Password must be at most 50 characters'),
    confirmPassword: yup.string().required('Confirmation of the new password is required').min(8, 'Password must be at least 8 characters').max(50, 'Password must be at most 50 characters').oneOf([yup.ref('newPassword')], "Passwords do not match"),
});

export const useChangePassword = () => {
    const {
        register,
        handleSubmit,
        watch,
        formState: {errors, isSubmitSuccessful},
        setError,
    } = useForm<Inputs>({
        resolver: yupResolver(schema),
    });

    const {data} = useSession()
    const userId = data?.user?.id
    const login = data?.user?.login

    const onSubmit: SubmitHandler<Inputs> = async (data) => {
        const res =
            await fetch(
                `${process.env.NEXT_PUBLIC_API_URL}/auth/change-password`,
                {
                    method: 'POST',
                    headers: {
                        Authorization: `Bearer ${process.env.NEXT_PUBLIC_API_KEY}`,
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({...data, login: login}),
                    cache: 'no-cache',
                },
            );

        const jsonData = await res.json();

        if (jsonData.error) {
            switch (jsonData.error) {
                case 'Please fill all fields':
                    setError('currentPassword', {type: 'manual', message: 'This field is required'});
                    setError('newPassword', {type: 'manual', message: 'This field is required'});
                    setError('confirmPassword', {type: 'manual', message: 'This field is required'});
                    break;
                case 'Invalid old password':
                    setError('currentPassword', {type: 'manual', message: 'Invalid old password'});
                    break;
                case 'New password cannot be the same as the old one':
                    setError('newPassword', {
                        type: 'manual',
                        message: 'New password cannot be the same as the old one'
                    });
                    break;
                case 'Passwords do not match':
                    setError('newPassword', {type: 'manual', message: 'Passwords do not match'});
                    setError('confirmPassword', {type: 'manual', message: 'Passwords do not match'});
                    break;
                case 'Password must be at least 8 characters long':
                    setError('newPassword', {type: 'manual', message: 'Password must be at least 8 characters long'});
                    break;
                case 'Password must be at most 50 characters long':
                    setError('newPassword', {type: 'manual', message: 'Password must be at most 50 characters long'});
                    break;
            }
        }
    };

    return {
        register,
        handleSubmit,
        watch,
        formState: {errors, isSubmitSuccessful},
        onSubmit,
    };
};
