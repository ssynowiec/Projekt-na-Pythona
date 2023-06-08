'use client'

import {Input} from "@/components/input/input";
import {Button} from "@/components/button/button";
import {useChangePassword} from "@/hooks/changePasswordHook";
import {AlertBox} from "@/components/alertBox/alertBox";

export const ChangePasswordForm = () => {
    const {register, handleSubmit, onSubmit, formState} = useChangePassword();

    return <>
        {formState.isSubmitSuccessful &&
            <AlertBox type='success' boldMessage='Success!' message='Your password has been changed.'/>}
        {!formState.isSubmitSuccessful && <>
            <form onSubmit={handleSubmit(onSubmit)}>

                <Input label='Current password' id='current_password' type='password'
                       placeholder="***********"
                       markAsRequired={true}
                       error={formState.errors.currentPassword?.message}
                       required={true} {...register('currentPassword')}/>
                <Input label='New password' id='new_password'
                       placeholder="***********"
                       markAsRequired={true}
                       error={formState.errors.newPassword?.message}
                       type='password'
                       required={true} {...register('newPassword')}/>
                <Input label='Repeat new password' id='repeat_new_password'
                       placeholder="***********"
                       markAsRequired={true}
                       error={formState.errors.confirmPassword?.message}
                       type='password'
                       required={true} {...register('confirmPassword')}/>
                <Button type='submit'>Update password</Button>
            </form>
            <p><span className="text-red-500">*</span> - This field is required</p>
        </>}

    </>
}
