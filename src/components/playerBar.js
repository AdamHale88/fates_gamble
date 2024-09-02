import player from "../player.json"
const PlayerBar = () => {
  return [...player].map((player) => (
    <>
      <nav className="uk-flex uk-flex-direction-column uk-justify-content-center uk-align-center uk-margin-remove">
        <li>{player.playerName}</li>
        <li>{player.wallet}</li>
      </nav>
    </>
  ));
};

export default PlayerBar;
