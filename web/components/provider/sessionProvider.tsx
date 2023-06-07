'use client';

import {
	SessionProvider as NextAuthSessionProvider,
	SessionProviderProps,
} from 'next-auth/react';

export const SessionProvider = ({ children }: SessionProviderProps) => {
	return <NextAuthSessionProvider>{children}</NextAuthSessionProvider>;
};
