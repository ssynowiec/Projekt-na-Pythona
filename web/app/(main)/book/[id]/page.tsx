import { Container } from '@/components/container/container';
import type { Metadata } from 'next';
import { BookDetails } from '@/components/bookDetails/bookDetails';
import { BookHeader } from '@/components/bookHeader/bookHeader';

type BookPageProps = { params: { id: string } };

const getBook = async (id: string) => {
	try {
		const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/book/${id}`, {
			method: 'GET',
			headers: {
				Authorization: `Bearer ${process.env.NEXT_PUBLIC_API_KEY}`,
				'Content-Type': 'application/json',
			},
			redirect: 'follow',
			cache: 'no-cache',
		});

		if (!res.ok) {
			throw new Error(`Could not fetch data, received ${res.status}`);
		}

		return res.json();
	} catch (error) {
		console.error(error);
	}
};

export const generateMetadata = async ({
	params,
}: BookPageProps): Promise<Metadata> => {
	const id = params.id;

	const book: Book = await getBook(id);

	return {
		title: book.title,
		openGraph: {
			// images: ['/some-specific-page-image.jpg', ...previousImages],
			images: ['/some-specific-page-image.jpg'],
		},
	};
};

const BookPage = async ({ params }: BookPageProps) => {
	const book: Book = await getBook(params.id);

	return (
		<Container>
			<BookHeader book={book} />
			<BookDetails book={book} />
		</Container>
	);
};

export default BookPage;
