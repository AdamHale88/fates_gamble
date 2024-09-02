import StartButton from "./startbutton";
const StartScreen = () => {
  return (
    <>
      <figure className="uk-section uk-section-small uk-flex uk-flex-column uk-justify-content-center uk-margin-remove uk-align-center">
        <div className=" logosub uk-flex uk-justify-content-center uk-align-center"></div>

        <legend className="uk-legend uk-justify-content-center uk-align-center uk-text-center">
          Fate's Gamble
        </legend>
        <div className="uk-flex uk-flex-column uk-justify-content-center uk-align-center">
          <img id="profile" src="images\logo.png" alt="pixel revolver" />
        </div>

        <div className="profile uk-flex uk-flex-column uk-justify-content-center uk-align-center">
          <form>
            <div class="uk-margin">
              <div class="uk-inline">
                <input
                  class="uk-input"
                  id="uk-input"
                  type="text"
                  placeholder="Player Name"
                  aria-label="Not clickable icon"
                ></input>
              </div>
            </div>
          </form>
          <div className="profile uk-flex uk-flex-column uk-justify-content-center uk-align-center">
            <StartButton />
          </div>
        </div>
      </figure>
    </>
  );
};

export default StartScreen;
