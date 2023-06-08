import {Heading} from "@/components/heading/heading";
import {ChangePasswordForm} from "@/components/changePasswordForm/changePasswordForm";

export const metadata = {
    title: 'Change your password',
    openGraph: {
        title: 'Change your password',
    },
};

const ChangePasswordPage = () => {
    return <>
        <Heading tag='h1' size='large'>Change password</Heading>
        <ChangePasswordForm/>
    </>
}

export default ChangePasswordPage
