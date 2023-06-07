import NextLink from 'next/link';
import type { ReactNode } from 'react';

type LinkProps = {
	type?: 'inline' | 'button';
	href: string;
	children: ReactNode;
};

export const Link = ({ type = 'inline', href, children }: LinkProps) => {
	if (type === 'inline')
		return (
			<NextLink
				href={href}
				className="font-semibold leading-6 text-indigo-600 hover:text-indigo-500"
			>
				{children}
			</NextLink>
		);
	else
		return (
			<a
				href={href}
				className="rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
			>
				{children}
			</a>
		);
};
