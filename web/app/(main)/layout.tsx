import { Inter } from 'next/font/google';
import { Header } from '@/components/header/header';
import { Footer } from '@/components/footer/footer';
import type { ReactNode } from 'react';

const inter = Inter({ subsets: ['latin'] });

export const metadata = {
	title: 'Library',
	description: 'Generated by create next app',
};

type RootLayoutProps = {
	children: ReactNode;
};

export default function RootLayout({ children }: RootLayoutProps) {
	return (
		<>
			<Header />
			{children}
			<Footer />
		</>
	);
}
