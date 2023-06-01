import { Inter } from 'next/font/google';
import { Header } from '../../components/header/header';
import { Footer } from '../../components/footer/footer';

const inter = Inter({ subsets: ['latin'] });

export const metadata = {
	title: 'Library',
	description: 'Generated by create next app',
};

export default function RootLayout({ children }: { children: ReactNode }) {
	return (
		<>
			<Header />
			{children}
			<Footer />
		</>
	);
}