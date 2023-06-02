import { Container } from '@/components/container/container';
import type { Metadata } from 'next';
import { BookDetails } from '@/components/bookDetails/bookDetails';
import { BookHeader } from '@/components/bookHeader/bookHeader';

type BookPageProps = { params: { id: string } };

const getBook = async (id: string) => {
	try {
		const res = await fetch(`${process.env.API_URL}/book/${id}`, {
			method: 'GET',
			headers: {
				Authorization: `Bearer ${process.env.API_KEY}`,
				'Content-Type': 'application/json',
			},
			redirect: 'follow',
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
}: BookPageProps): // parent?: ResolvingMetadata,
Promise<Metadata> => {
	// read route params
	const id = params.id;

	// fetch data
	const book: Book = await getBook(id);

	// optionally access and extend (rather than replace) parent metadata
	// const previousImages = (await parent).openGraph?.images || [];

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
