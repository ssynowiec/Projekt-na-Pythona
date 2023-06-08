'use client'

import {signOut} from 'next-auth/react';
import {useEffect} from 'react';
import {redirect} from "next/navigation";
import {Header} from "@/components/header/header";
import {Container} from "@/components/container/container";
import {Heading} from "@/components/heading/heading";
import {Footer} from "@/components/footer/footer";

export default function Logout() {
    // const router = useRouter();

    useEffect(() => {
        signOut({callbackUrl: '/'});
        // Przekierowanie na inną stronę po wylogowaniu (np. na stronę główną)
        redirect('/');
    }, []);

    return <>
        <Header/>
        <Container>
            <Heading tag='h1' size='large'>
                Logout
            </Heading>
        </Container>
        <Footer/>
    </>;
}
