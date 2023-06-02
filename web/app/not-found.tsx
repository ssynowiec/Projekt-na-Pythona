import { Link } from '@/components/link/link';
import { Heading } from '@/components/heading/heading';

const NotFound = () => {
	return (
		<>
			<main className="grid min-h-screen place-items-center bg-white px-6 py-24 sm:py-32 lg:px-8">
				<div className="text-center">
					<p className="text-base font-semibold text-indigo-600">404</p>
					<Heading tag="h1" size="large" className="text-3xl sm:text-5xl">
						Page not found
					</Heading>
					<p className="mt-6 text-base leading-7 text-gray-600">
						Sorry, we couldn’t find the page you’re looking for.
					</p>
					<div className="mt-10 flex items-center justify-center gap-x-6">
						<Link href="/" type="button">
							Go back home
						</Link>
						<Link href="#">
							Contact support <span aria-hidden="true">&rarr;</span>
						</Link>
					</div>
				</div>
			</main>
		</>
	);
};

export default NotFound;
