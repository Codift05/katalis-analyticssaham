export const useSentimentFilter = () => {
  return useState<string | null>('sentimentFilter', () => null);
};
