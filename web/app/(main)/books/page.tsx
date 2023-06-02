import { Container } from '@/components/container/container';
import { Link } from '@/components/link/link';
import { Heading } from '@/components/heading/heading';

const getData = async () => {
	try {
		const res = await fetch(`${process.env.API_URL}/books`, {
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

const BooksPage = async () => {
	const data: Book[] = await getData();

	return (
		<Container>
			<Heading tag="h1" size="large">
				Book list
			</Heading>
			<ul>
				{data.map((book) => (
					<li key={book.id}>
						<Link href={`/book/${book.id}`}>{book.title}</Link>
					</li>
				))}
			</ul>
		</Container>
	);
};

export default BooksPage;
