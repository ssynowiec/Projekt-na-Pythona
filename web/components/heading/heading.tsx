import type { HTMLAttributes, ReactNode } from 'react';
import clsx from 'clsx';

type TextSize = 'small' | 'medium' | 'large';

type HeadingTag = 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'h6';

type HeadingProps = {
	tag: HeadingTag;
	size: TextSize;
	children: ReactNode;
	className?: string;
} & HTMLAttributes<HTMLHeadingElement>;

export const Heading = ({
	tag: Tag,
	size,
	children,
	className,
	...rest
}: HeadingProps) => {
	return (
		<Tag
			className={clsx(
				{
					'text-sm': size === 'small',
					'text-base': size === 'medium',
					'text-2xl': size === 'large',
				},
				'font-bold',
				className,
			)}
			{...rest}
		>
			{children}
		</Tag>
	);
};
