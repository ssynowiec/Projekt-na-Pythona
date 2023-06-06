import { ChangeEvent, forwardRef } from 'react';

type InputProps = {
	label: string;
	id: string;
	name: string;
	type: string;
	autoComplete?: string;
	required: boolean;
	placeholder?: string;
	onChange: (e: ChangeEvent<HTMLInputElement>) => void;
};

export const Input = forwardRef<HTMLInputElement, InputProps>(
	(
		{
			label,
			id,
			name,
			type = 'text',
			autoComplete,
			required,
			placeholder,
			onChange,
			...rest
		},
		ref,
	) => {
		return (
			<div>
				<label
					htmlFor={id}
					className="block text-sm font-medium leading-6 text-gray-900"
				>
					{label}
				</label>
				<div className="mt-2">
					<input
						ref={ref}
						id={id}
						type={type}
						autoComplete={autoComplete}
						required={required}
						placeholder={placeholder}
						onChange={onChange}
						name={name}
						{...rest}
						className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
					/>
				</div>
			</div>
		);
	},
);
