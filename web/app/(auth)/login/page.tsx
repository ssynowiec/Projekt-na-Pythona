import { Input } from '@/components/input/input';
import { Button } from '@/components/button/button';
import { Logo } from '@/components/logo/logo';
import { Link } from '@/components/link/link';
import { Heading } from '@/components/heading/heading';

export const metadata = {
	title: 'Log in to Library',
	openGraph: {
		title: 'Log in to Library',
	},
};

const LoginPage = () => {
	return (
		<>
			<div className="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
				<div className="sm:mx-auto sm:w-full sm:max-w-sm">
					<Logo />
					<Heading
						tag="h1"
						size="large"
						className="text-center mt-10 tracking-tight"
					>
						Login in to Library
					</Heading>
				</div>

				<div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
					<form className="space-y-6" action="#" method="POST">
						<Input
							label="Email address or login"
							id="email"
							name="email"
							type="email"
							autoComplete="email"
							required={true}
							placeholder="jan.kowalski@example.com"
						/>

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
									name="password"
									type="password"
									autoComplete="current-password"
									required
									placeholder="***********"
									className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
								/>
							</div>
						</div>
						<Button type="submit">Log in</Button>
					</form>

					<p className="mt-10 text-center text-sm text-gray-500">
						<Link href="/">&larr; Back to Home page</Link>
					</p>
				</div>
			</div>
		</>
	);
};

export default LoginPage;
