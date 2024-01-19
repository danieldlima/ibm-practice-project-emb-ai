const runSentimentAnalysis = async () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const response = await fetch(`sentimentAnalyzer?textToAnalyze=${textToAnalyze}`);

    const texSentiment = document.getElementById("system_response")
    const textError = document.getElementById("system_response_error")

    if (response.status === 200) {
      const { data } = await response.json();

      textError.innerHTML = ''
      textError.style.setProperty('display', 'none');

      texSentiment.style.setProperty('display', 'block')
      texSentiment.innerHTML = data.label;
    } else if (response.status === 400) {
      const data = await response.json();

      texSentiment.innerHTML = '';
      texSentiment.style.setProperty('display', 'none')

      textError.style.setProperty('display', 'block')
      textError.innerHTML = data.message;
    } else {
      console.error('runSentimentAnalysis(): Request to endpoint sentimentAnalyzer failed!');
    }
};
