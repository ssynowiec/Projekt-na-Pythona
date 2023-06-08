'use client';

import { NavLink } from '@/components/navLink/navLink';
import { useSession } from 'next-auth/react';

const readerNavLinks: NavLink[] = [
	{ href: '/your-profile', label: 'Your data' },
	{ href: '/change-password', label: 'Change password' },
	{ href: '/my-rentals', label: 'My rentals' },
	{ href: '/my-reservations', label: 'My reservations' },
	{ href: '/settings', label: 'Settings' },
	{ href: '/logout', label: 'Logout' },
];
const adminNavLinks: NavLink[] = [{ href: '/your-profile', label: 'Your data' }, {
	href: '/change-password',
	label: 'Change password',
}, {
	href: '/rental',
	label: 'Rental',
}, {
	href: '/reservations',
	label: 'Reservation',
}, {
	href: 'books/add',
	label: 'Add new book',
}, {
	href: '/books',
	label: 'All books',
}, { href: '/readers', label: 'Add new reader' }, { href: '/readers', label: 'All readers' }, {
	href: '/logout',
	label: 'Logout',
}];


export const DashboardMenu = () => {
	const { data } = useSession();
	const role = data?.user?.role;

	const navLinks: NavLink[] = role === 'admin' ? adminNavLinks : readerNavLinks;

	return <nav>
		<ul>
			{navLinks.map((link, i) => (
				<li key={i}>
					<NavLink label={link.label} href={link.href} />
				</li>))}
		</ul>
	</nav>;
};
