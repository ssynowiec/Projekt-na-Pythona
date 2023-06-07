import {ChangeEvent, forwardRef} from 'react';
import clsx from 'clsx';

type InputProps = {
    label: string;
    id: string;
    name: string;
    type: string;
    autoComplete?: string;
    required: boolean;
    placeholder?: string;
    error?: string;
    disabled?: boolean;
    value?: string;
    onChange?: (e: ChangeEvent<HTMLInputElement>) => void;
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
            error,
            disabled = false,
            value,
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
                        disabled={disabled}
                        value={value}
                        {...rest}
                        className={clsx(
                            'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',
                            error && 'ring-2 ring-red-500',
                            disabled && 'bg-gray-100',
                        )}
                    />
                </div>
                {error && (
                    <p className="mt-1 text-sm text-red-600" id="email-error">
                        {error}
                    </p>
                )}
            </div>
        );
    },
);
