const runSentimentAnalysis = async () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const response = await fetch(`sentimentAnalyzer?textToAnalyze=${textToAnalyze}`);

    const texSentiment = document.getElementById("system_response")
    const textError = document.getElementById("system_response_error")

    if (response.status === 200) {
      const { data } = await response.json();

      textError.innerHTML = ''
      texSentiment.innerHTML = data.label;
    } else if (response.status === 400) {
      const data = await response.json();

      texSentiment.innerHTML = '';
      textError.innerHTML = data.message;
    } else {
      console.error('runSentimentAnalysis(): Request to endpoint sentimentAnalyzer failed!');
    }
};
