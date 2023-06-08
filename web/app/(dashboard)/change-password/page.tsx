import {Heading} from "@/components/heading/heading";
import {Input} from "@/components/input/input";
import {Button} from "@/components/button/button";

const ChangePasswordPage = () => {
    return <>
        <Heading tag='h1' size='large'>Change password</Heading>
        <form>

            <Input label='Current password' id='current_password' name='current_password' type='password'
                   placeholder="***********"
                   required={true}/>
            <Input label='New password' id='new_password' name='new_password'
                   placeholder="***********"
                   type='password'
                   required={true}/>
            <Input label='Repeat new password' id='repeat_new_password'
                   placeholder="***********"
                   name='repeat_new_password' type='password'
                   required={true}/>
            <Button type='submit'>Update password</Button>
        </form>
    </>
}

export default ChangePasswordPage
