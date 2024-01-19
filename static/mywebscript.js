const runSentimentAnalysis = async () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const response = await fetch(`sentimentAnalyzer?textToAnalyze=${textToAnalyze}`);

    if (response.status === 200) {
      const { data } = await response.json();
      document.getElementById("system_response").innerHTML = data.label;
    } else {
      console.error('runSentimentAnalysis(): Request to endpoint sentimentAnalyzer failed!');
    }
};
