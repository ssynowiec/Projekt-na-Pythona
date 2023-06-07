import type { ReactNode } from 'react';

type BaseButtonProps = {
	children: ReactNode;
	disabled?: boolean;
};

type ButtonPropsTypeSubmit = {
	onClick?: () => void;
	type: 'submit';
};

type ButtonPropsTypeButton = {
	type?: 'button';
	onClick: () => void;
};

type ButtonProps = (ButtonPropsTypeSubmit | ButtonPropsTypeButton) &
	BaseButtonProps;

export const Button = ({ type, children }: ButtonProps) => {
	return (
		<button
			type={type}
			className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
		>
			{children}
		</button>
	);
};
