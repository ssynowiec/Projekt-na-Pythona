'use client';

import { Input } from '@/components/input/input';
import { Link } from '@/components/link/link';
import { Button } from '@/components/button/button';
import { useLogin } from '@/hooks/loginHook';

export const LoginForm = () => {
	const { handleSubmit, onSubmit, watch, formState, register } = useLogin();

	return (
		<form
			className="space-y-6"
			action="#"
			method="POST"
			onSubmit={handleSubmit(onSubmit)}
		>
			<Input
				label="Email address or login"
				id="email"
				type="text"
				autoComplete="email"
				required={true}
				placeholder="jan.kowalski@example.com"
				{...register('email', { required: true })}
			/>
			{/*{errors.email && <span>This field is required</span>}*/}

			<div>
				<div className="flex items-center justify-between">
					<label
						htmlFor="password"
						className="block text-sm font-medium leading-6 text-gray-900"
					>
						Password
					</label>
					<div className="text-sm">
						<Link href="/forgot-password">Forgot password?</Link>
					</div>
				</div>
				<div className="mt-2">
					<input
						id="password"
						type="password"
						autoComplete="current-password"
						required
						placeholder="***********"
						{...register('password', { required: true })}
						className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
					/>
				</div>
			</div>
			<Button type="submit">Log in</Button>
		</form>
	);
};
