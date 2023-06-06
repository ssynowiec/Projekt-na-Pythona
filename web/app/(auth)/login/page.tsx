import { Logo } from '@/components/logo/logo';
import { Link } from '@/components/link/link';
import { Heading } from '@/components/heading/heading';
import { LoginForm } from '@/components/loginForm/loginForm';

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
					<LoginForm />
					<p className="mt-10 text-center text-sm text-gray-500">
						<Link href="/">&larr; Back to Home page</Link>
					</p>
				</div>
			</div>
		</>
	);
};

export default LoginPage;
