import { Container } from '@/components/container/container';

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

const Page = async () => {
	const data: Book[] = await getData();

	return (
		<div>
			<Container>
				<h1>Book List</h1>
				<ul>
					{data.map((book) => (
						<li key={book.id}>
							<a>{book.title}</a>
						</li>
					))}
				</ul>
			</Container>
		</div>
	);
};

export default Page;
