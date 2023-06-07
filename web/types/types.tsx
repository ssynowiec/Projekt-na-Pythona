type Book = {
	id: number;
	author: string;
	publisher: number;
	title: string;
	description?: string;
	publication_date: string;
	genre: string;
	is_available: string;
	number_of_pages: number;
	cover_image: string;
	ISBN: string;
};

type NavLink = {
	href: string;
	label: string;
};
