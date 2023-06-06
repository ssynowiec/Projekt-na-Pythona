import { Heading } from '@/components/heading/heading';
import Image from 'next/image';

type BookHeaderProps = {
	book: Book;
};

export const BookHeader = ({ book }: BookHeaderProps) => {
	const blobUrl = `data:image/jpeg;base64,${book.cover_image}`;

	return (
		<section className="w-full flex justify-around">
			<Image
				src={blobUrl}
				alt={book.title}
				width={1000}
				height={1000}
				className="rounded-lg w-1/4"
			/>
			<div className="w-2/4">
				<Heading tag="h1" size="large">
					{book.title}
				</Heading>
				<p className="mt-1 max-w-2xl text-sm leading-6 text-gray-500">
					{book.description}
				</p>
			</div>
		</section>
	);
};
