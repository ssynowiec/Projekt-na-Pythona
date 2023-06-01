'use client';

import type { ReactNode } from 'react';

type ContainerProps = {
	children: ReactNode;
};

export const Container = ({ children }: ContainerProps) => {
	return (
		<div className="mx-auto flex flex-col max-w-7xl items-center justify-between p-6 lg:px-8">
			{children}
		</div>
	);
};
