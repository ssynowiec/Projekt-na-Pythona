import clsx from "clsx";

type AlertBoxProps = {
    type: 'success' | 'error' | 'warning'
    boldMessage: string
    message: string
}

export const AlertBox = ({type, boldMessage, message}: AlertBoxProps) => {
    const typeStyle = clsx({
        'text-green-900 border-green-300 bg-green-50 dark:text-green-500': type === 'success',
        'text-red-900 border-red-300 bg-red-50 dark:text-red-500': type === 'error',
        'text-yellow-900 border-yellow-300 bg-yellow-50 dark:text-yellow-500': type === 'warning',
    })

    return <div
        className={clsx("flex p-4 mb-4 my-5 text-sm border rounded-lg", typeStyle)}
        role="alert">
        <svg aria-hidden="true" className="flex-shrink-0 inline w-5 h-5 mr-3" fill="currentColor"
             viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fillRule="evenodd"
                  d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
                  clipRule="evenodd"></path>
        </svg>
        <span className="sr-only">{type}</span>
        <div>
            <span className="font-medium">{boldMessage}</span> {message}
        </div>
    </div>
}
