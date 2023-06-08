import {SubmitHandler, useForm} from 'react-hook-form';
import {yupResolver} from '@hookform/resolvers/yup';
import * as yup from 'yup';

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
        formState: {errors},
        setError,
    } = useForm<Inputs>({
        resolver: yupResolver(schema),
    });

    const onSubmit: SubmitHandler<Inputs> = async (data) => {
        const res = await fetch('/api/auth/change-password', {});

        console.log(res);

        return res;
    };

    return {
        register,
        handleSubmit,
        watch,
        formState: {errors},
        onSubmit,
    };
};
