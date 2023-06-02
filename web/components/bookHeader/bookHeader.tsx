import { Heading } from '@/components/heading/heading';
import Image from 'next/image';

type BookHeaderProps = {
	book: Book;
};

export const BookHeader = ({ book }: BookHeaderProps) => {
	return (
		<section className="w-full flex justify-around">
			{/* TODO: Add dynamic image support */}
			<Image
				src="/harry-potter-i-kamien-filozoficzny-tom-1.jpg"
				// src={book.cover}
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
					"Harry Potter i Kamień Filozoficzny" to pierwsza część niezwykle
					popularnej serii książek napisanych przez J.K. Rowling. Opowieść
					rozpoczyna się, gdy sierota o imieniu Harry Potter dowiaduje się, że
					jest czarodziejem i zostaje przyjęty do Hogwartu, szkoły magii i
					czarodziejstwa. Wraz z przyjaciółmi Hermioną Granger i Ronem
					Weasleyem, Harry wchodzi w świat pełen tajemnic, magii i
					niebezpieczeństw. Głównym wątkiem książki jest poszukiwanie
					tajemniczego Kamienia Filozoficznego, który daje niezwykłą moc swojemu
					posiadaczowi. Czy Harry i jego przyjaciele zdołają odkryć tajemnice,
					które kryje szkoła i pokonać złego Lorda Voldemorta? "Harry Potter i
					Kamień Filozoficzny" to fascynująca i pełna przygód historia, która
					wprowadza czytelników w magiczny świat Hogwartu.
				</p>
			</div>
		</section>
	);
};
