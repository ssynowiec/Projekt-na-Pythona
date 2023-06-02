import { BookDetailElement } from '@/components/bookDetails/bookDetailElement';
import { Heading } from '@/components/heading/heading';

type BookDetailsProps = {
	book: Book;
};

type DetailBook = {
	name: string;
	value: string;
};

export const BookDetails = ({ book }: BookDetailsProps) => {
	const bookDetails: DetailBook[] = [
		{ name: 'Full title', value: book.title },
		{ name: 'Author', value: book.author },
		{ name: 'Number of pages', value: book.pages },
		{ name: 'Date of publication', value: book.publicationDate },
		{ name: 'Publishing house', value: book.publishingHouse },
	];

	return (
		<div className="w-full mt-20">
			<div className="px-4 sm:px-0">
				<Heading tag="h3" size="medium">
					Book details
				</Heading>
				<p className="mt-1 max-w-2xl text-sm leading-6 text-gray-500">
					{/*Personal details and application.*/}
				</p>
			</div>
			<div className="mt-6 border-t border-gray-100 w-full">
				<dl className="divide-y divide-gray-100 w-full">
					{bookDetails.map((detail) => {
						return (
							<BookDetailElement name={detail.name} value={detail.value} />
						);
					})}
				</dl>
			</div>
		</div>
	);
};
