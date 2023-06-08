'use client'

import {Heading} from "@/components/heading/heading";
import {Input} from "@/components/input/input";
import {useSession} from "next-auth/react";

const DashboardPage = () => {
    const {data, status} = useSession();
    console.log(data?.user)

    return (
        <>

            <Heading tag='h1' size='large'>Your Profile</Heading>
            <form className='flex flex-col'>
                <Heading tag='h2' size='large'>Personal Information</Heading>

                <div className='flex flex-col md:flex-row justify-between'>
                    <Input label='Your name' id='name' name='name' type='text' required={true}
                           disabled={true}
                           value={data?.user?.name}/>
                    <Input label='Your surname' id='surname' name='surname' type='text' required={true}
                           disabled={true}
                           value={data?.user?.surname}/>
                </div>
                <Input label='Bithday' id='birthday' name='birthday' type='date' required={true}
                       disabled={true}
                       value={data?.user?.birthday}/>

                <Heading tag='h2' size='large'>Contact information</Heading>

                <Input label='Your address email' id='email' name='email' type='email' required={true}
                       value={data?.user?.email} disabled={true}/>
                <Input label='Your phone number' id='phone' name='phone' type='tel' required={true}
                       value={data?.user?.phone_number} disabled={true}/>

                <Heading tag='h2' size='large'>Address</Heading>

                <Input label='Your address' id='street' name='street' type='text' required={true}
                       value={data?.user?.address_street} disabled={true}/>
                <div className='flex flex-col md:flex-row justify-between'>
                    <Input label='Postal code' id='postal_code' name='postal_code' type='tel' required={true}
                           value={data?.user?.postal_code} disabled={true}/>
                    <Input label='City' id='city' name='city' type='text' required={true}
                           value={data?.user?.city} disabled={true}/>
                </div>

                <Heading tag='h2' size='large'>Other informations</Heading>

                <div className='flex flex-col md:flex-row justify-between'>
                    <Input label='Login' id='login' name='login' type='text' required={true}
                           value={data?.user?.login} disabled={true}/>
                    <Input label='Password' id='password' name='password' type='password' required={true}
                           value={data?.user?.password} disabled={true}/>
                </div>
                <Input label='Card number' id='card_number' name='card_number' type='text' required={true}
                       value={data?.user?.card_number} disabled={true}/>
            </form>
        </>
    );
};

export default DashboardPage;
