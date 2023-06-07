import NextAuth, { type NextAuthOptions } from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';

const options: NextAuthOptions = {
	session: {
		strategy: 'jwt',
	},
	providers: [
		CredentialsProvider({
			type: 'credentials',
			credentials: {
				login: { label: 'Login', type: 'text' },
				password: { label: 'Password', type: 'password' },
			},
			async authorize(credentials, req) {
				if (!credentials) return null;
				const { login, password } = credentials;
				const response = await fetch(
					`${process.env.NEXT_PUBLIC_API_URL}/auth/login`,
					{
						method: 'POST',
						headers: {
							Authorization: `Bearer ${process.env.NEXT_PUBLIC_API_KEY}`,
							'Content-Type': 'application/json',
						},
						body: JSON.stringify(credentials),
						cache: 'no-cache',
					},
				);

				const data = await response.json();

				if (data.error) {
					throw new Error(data.error);
				}

				return data;
			},
		}),
	],
	secret: process.env.NEXTAUTH_SECRET,
	pages: {
		signIn: '/login',
		error: '/login',
	},
	callbacks: {
		async jwt({ token, user }) {
			return { ...token, ...user };
		},
		async session({ session, token }) {
			session.user = token;

			return session;
		},
		// async redirect({ url, baseUrl }) {
		// 	// if (url.startsWith(baseUrl)) {
		// 	// 	return url;
		// 	// }
		// 	if (url.startsWith('/')) return `${baseUrl}${url}`;
		// 	// Allows callback URLs on the same origin
		// 	else if (new URL(url).origin === baseUrl) return url;
		// 	return baseUrl;
		// },
	},
};

const handler = NextAuth(options);

export { handler as GET, handler as POST };
