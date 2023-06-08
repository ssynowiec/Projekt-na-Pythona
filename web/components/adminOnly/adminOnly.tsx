'use client';

import { useSession } from 'next-auth/react';
import { ReactNode, useEffect } from 'react';
import { redirect } from 'next/navigation';
import { Loading } from '@/components/loading/loading';
import { Header } from '@/components/header/header';
import { Footer } from '@/components/footer/footer';
import { Container } from '@/components/container/container';

type AdminOnlyProps = {
	children: ReactNode;
};

export const AdminOnly = ({ children }: AdminOnlyProps) => {
	const { status, data } = useSession();

	useEffect(() => {
		if (status === 'unauthenticated') {
			redirect('/login');
		}
	}, [status]);

	if (status === 'authenticated' && data?.user?.role === 'admin') {
		return <>{children}</>;
	} else if (status === 'authenticated' && data?.user?.role !== 'admin') {
		redirect('/your-profile');
	}

	return (
		<>
			<Header />
			<main className='h-screen'>
				<Container>
					<Loading />
				</Container>
			</main>
			<Footer />
		</>
	);
};
