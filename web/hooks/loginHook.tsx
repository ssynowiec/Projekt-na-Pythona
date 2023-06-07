import { SubmitHandler, useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import * as process from 'process';

type Inputs = {
	email: string;
	password: string;
};

const schema = yup.object({
	email: yup.string().required(),
	password: yup.string().required(),
});

export const useLogin = () => {
	const {
		register,
		handleSubmit,
		watch,
		formState: { errors },
	} = useForm<Inputs>({
		resolver: yupResolver(schema),
	});

	const onSubmit: SubmitHandler<Inputs> = async (data) => {
		try {
			const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/auth/login`, {
				method: 'POST',
				headers: {
					Authorization: `Bearer ${process.env.NEXT_PUBLIC_API_KEY}`,
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({
					login: data.email,
					password: data.password,
				}),
				redirect: 'follow',
				cache: 'no-cache',
			});
			const json = await res.json();
			console.log(json.message);
		} catch (error) {
			console.log(error);
		}
	};

	return {
		register,
		handleSubmit,
		watch,
		formState: { errors },
		onSubmit,
	};
};
