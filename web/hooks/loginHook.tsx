import { SubmitHandler, useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import { signIn } from 'next-auth/react';

type Inputs = {
	login: string;
	password: string;
};

const schema = yup.object({
	login: yup.string().required('Email or login is required'),
	password: yup.string().required('Password is required'),
});

export const useLogin = () => {
	const {
		register,
		handleSubmit,
		watch,
		formState: { errors },
		setError,
	} = useForm<Inputs>({
		resolver: yupResolver(schema),
	});

	const onSubmit: SubmitHandler<Inputs> = async (data) => {
		const res = await signIn('credentials', {
			login: data.login,
			password: data.password,
			// redirect: false,
			callbackUrl: '/dashboard',
		});

		console.log(res);

		if (res?.error) {
			if (res.error === 'Invalid login or email') {
				setError('login', { message: res.error });
			} else if (res.error === 'Incorrect password') {
				setError('password', { message: res.error });
			}
		}

		return res;
	};

	return {
		register,
		handleSubmit,
		watch,
		formState: { errors },
		onSubmit,
	};
};
