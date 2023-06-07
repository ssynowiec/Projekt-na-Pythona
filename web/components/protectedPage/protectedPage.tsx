'use client';

import { useSession } from 'next-auth/react';
import { ReactNode, useEffect } from 'react';
import { redirect } from 'next/navigation';

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

	return <p>Loading...</p>;
};
