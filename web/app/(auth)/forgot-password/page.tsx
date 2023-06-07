import { Input } from '@/components/input/input';
import { Button } from '@/components/button/button';
import { Logo } from '@/components/logo/logo';
import { Link } from '@/components/link/link';
import { Heading } from '@/components/heading/heading';

export const metadata = {
	title: 'Forgot Password',
	openGraph: {
		title: 'Forgot Password',
	},
};

const ForgotPasswordPage = () => {
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
						Reset your password
					</Heading>
				</div>

				<div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
					<form className="space-y-6" action="#" method="POST">
						<Input
							label="Email address"
							id="email"
							name="email"
							type="email"
							autoComplete="email"
							required={true}
							placeholder="jan.kowalski@example.com"
						/>
						<Button type="submit">Reset password</Button>
					</form>

					<p className="mt-10 text-center text-sm text-gray-500">
						<Link href="/login">&larr; Back to login</Link>
					</p>
				</div>
			</div>
		</>
	);
};

export default ForgotPasswordPage;
