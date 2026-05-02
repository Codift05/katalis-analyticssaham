export type NewsItem = {
  id: number;
  source: string;
  title: string;
  sentiment: string;
  created_at?: string | null;
};

export const useNews = () => {
  const config = useRuntimeConfig();
  return useFetch<NewsItem[]>("/news", {
    baseURL: config.public.apiBase as string,
    default: () => []
  });
};
