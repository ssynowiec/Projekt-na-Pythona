import type { ReactNode } from 'react';
import { ProtectedPage } from '@/components/protectedPage/protectedPage';
import { Header } from '@/components/header/header';
import { Footer } from '@/components/footer/footer';
import { Container } from '@/components/container/container';
import { DashboardMenu } from '@/components/dashboardMenu/dashboardMenu';

export const metadata = {
	title: 'Library',
	description: 'Generated by create next app',
};

type LayoutProps = {
	children: ReactNode;
};

const DashboardLayout = ({ children }: LayoutProps) => {
	return (
		<ProtectedPage>
			<Header />
			<main className='min-h-screen'><Container>
				<div className='flex w-full flex-col md:flex-row'>
					<section className='w-full md:w-1/4'>
						<DashboardMenu />
					</section>
					<section className='w-full md:w-2/4 md:px-20'>
						{children}
					</section>
				</div>
			</Container></main>
			<Footer />
		</ProtectedPage>
	);
};

export default DashboardLayout;
