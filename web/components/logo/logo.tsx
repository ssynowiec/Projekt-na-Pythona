import Image from 'next/image';

export const Logo = () => {
	return (
		<Image
			src="/logo.png"
			alt=""
			width={1000}
			height={1000}
			className="mx-auto h-10 w-auto"
		/>
	);
};
