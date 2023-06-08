import {Link} from "@/components/link/link";

type NavLinkProps = NavLink;

export const NavLink = ({href, label}: NavLinkProps) => {
    return (
        <Link
            href={href}
            className="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
        >
            {label}
        </Link>
    )
}
