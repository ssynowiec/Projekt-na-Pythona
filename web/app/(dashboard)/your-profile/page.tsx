'use client'

import {Container} from '@/components/container/container';
import {Heading} from "@/components/heading/heading";
import {Input} from "@/components/input/input";
import {useSession} from "next-auth/react";

const DashboardPage = () => {
    const {data, status} = useSession();

    return (
        <Container>
            <div className='flex'>
                <section>Nav</section>
                <section><Heading tag='h1' size='large'>Your Profile</Heading>
                    <form>
                        <div className='flex flex-col md:flex-row'>
                            <Input label='Your name' id='name' name='name' type='text' required={true} disabled={true}
                                   value={data?.user?.name}/>
                            <Input label='Your surname' id='surname' name='surname' type='text' required={true}
                                   disabled={true}
                                   value={data?.user?.surname}/>
                        </div>
                    </form>
                </section>
            </div>
        </Container>
    );
};

export default DashboardPage;
