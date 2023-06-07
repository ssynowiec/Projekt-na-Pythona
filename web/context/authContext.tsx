import { createContext, type ReactNode, useState } from 'react';

type AuthProviderProps = {
	children: ReactNode;
};

export const AuthContext = createContext({});

export const AuthProvider = ({ children }: AuthProviderProps) => {
	const [token, setToken] = useState<string | null>(null);

	const login = (token: string) => {
		setToken(token);
	};

	const logout = () => {
		setToken(null);
	};

	return (
		<AuthContext.Provider value={{ token, login, logout }}>
			{children}
		</AuthContext.Provider>
	);
};
