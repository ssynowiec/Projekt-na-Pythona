import { AdminOnly } from '@/components/adminOnly/adminOnly';
import { ReactNode } from 'react';

type EmployeeLayoutProps = {
	children: ReactNode
}

const EmployeeLayout = ({ children }: EmployeeLayoutProps) => {
	return <AdminOnly>{children}</AdminOnly>;
};

export default EmployeeLayout;
