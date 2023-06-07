'use client';

import { useSession } from 'next-auth/react';
import { ReactNode, useEffect } from 'react';
import { redirect } from 'next/navigation';
import { Loading } from '@/components/loading/loading';
import { Header } from '@/components/header/header';
import { Footer } from '@/components/footer/footer';
import { Container } from '@/components/container/container';

type ProtectedPageProps = {
	children: ReactNode;
};

export const ProtectedPage = ({ children }: ProtectedPageProps) => {
	const { status, data } = useSession();
	console.log(status);

	useEffect(() => {
		if (status === 'unauthenticated') {
			redirect('/login');
		}
	}, [status]);

	if (status === 'authenticated') {
		return <>{children}</>;
	}

	return (
		<>
			<Header />
			<main className="h-screen">
				<Container>
					<Loading />
				</Container>
			</main>
			<Footer />
		</>
	);
};
