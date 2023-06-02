import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.List;
import java.util.Scanner;
import java.util.ArrayList;
import java.io.FileWriter;
import java.nio.file.Path;
import java.nio.file.Paths;
import zemberek.morphology.TurkishMorphology;
import zemberek.morphology.analysis.SingleAnalysis;
import zemberek.morphology.analysis.WordAnalysis;
import zemberek.normalization.TurkishSentenceNormalizer;

public class TweetDesigner {

    public static void main(String[] args) throws IOException {
        ArrayList <String> stopWords = new ArrayList<>(0);
        File stopWordFile = new File("/Users/eren/Desktop/twitter-research/stopWords.txt");
        Scanner stopWordParser = new Scanner(stopWordFile);
        while (stopWordParser.hasNextLine()) {
            stopWords.add(stopWordParser.nextLine());
        }

        Path lookupRoot = Paths.get("/Users/eren/Desktop/normalization");
        Path lmFile = Paths.get("/Users/eren/Desktop/lm.2gram.slm");
        TurkishMorphology morphology = TurkishMorphology.createWithDefaults();
        TurkishSentenceNormalizer normalizer = new TurkishSentenceNormalizer(morphology, lookupRoot, lmFile);

        FileWriter writer = new FileWriter("df.txt");
        ArrayList <String> tweetSet = csvReader();
        TurkishMorphology m = TurkishMorphology.createWithDefaults();
        for (String tweet : tweetSet) {
            tweet = normalizer.normalize(tweet);
            String[] words = tweet.split(" ");
            StringBuilder sentence = new StringBuilder();
            for (String word : words) {
                WordAnalysis result = m.analyze(word);
                List<SingleAnalysis> analysis = result.getAnalysisResults();
                if (word.equals("xgülücük") || word.equals("xüzülcük") || word.equals("corona") || word.equals("korona") || word.equals("covid")) {
                    sentence.append(word);
                } else if (!analysis.isEmpty()) {
                    String toAppend = analysis.get(0).getLemmas().get(analysis.get(0).getLemmas().size() - 1);
                    if (!isStopWord(toAppend,stopWords)) {
                        sentence.append(toAppend);
                        sentence.append(' ');
                    }
                }
            }
            writer.write(sentence + System.lineSeparator());
        }
        writer.close();
    }

    private static ArrayList<String> csvReader() {
        ArrayList <String> words = new ArrayList<>(0);
        try {
            File minedTweets = new File("/Users/eren/Desktop/df.txt");
            Scanner parser = new Scanner(minedTweets);
            parser.useDelimiter("\n");
            while (parser.hasNext()) {
                String word = parser.next();
                words.add(word);
            }
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        return words;
    }

    private static boolean isStopWord(String s, ArrayList<String> wordList) {
        boolean ans = false;
        for (String word : wordList) {
            if (s.equals(word)) {
                 ans = true;
                 break;
            }
        }
        return ans;
    }
}
