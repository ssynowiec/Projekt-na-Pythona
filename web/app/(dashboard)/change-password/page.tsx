import {Heading} from "@/components/heading/heading";
import {Input} from "@/components/input/input";
import {Button} from "@/components/button/button";

export const metadata = {
    title: 'Change your password',
    openGraph: {
        title: 'Change your password',
    },
};

const ChangePasswordPage = () => {
    return <>
        <Heading tag='h1' size='large'>Change password</Heading>
        <form>

            <Input label='Current password' id='current_password' name='current_password' type='password'
                   placeholder="***********"
                   markAsRequired={true}
                   required={true}/>
            <Input label='New password' id='new_password' name='new_password'
                   placeholder="***********"
                   markAsRequired={true}
                   type='password'
                   required={true}/>
            <Input label='Repeat new password' id='repeat_new_password'
                   placeholder="***********"
                   markAsRequired={true}
                   name='repeat_new_password' type='password'
                   required={true}/>
            <Button type='submit'>Update password</Button>
        </form>
        <p><span className="text-red-500">*</span> - This field is required</p>
    </>
}

export default ChangePasswordPage
