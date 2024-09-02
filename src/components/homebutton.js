/* eslint-disable jsx-a11y/anchor-is-valid */
import { Link } from "react-router-dom";

const HomeButton = () => {
  return (
    <>
      <nav className="uk-flex uk-flex-direction-column uk-justify-content-center uk-align-center uk-margin-remove">
        <ul className="uk-iconnav uk-flex uk-flex-direction-row uk-align-center uk-margin-remove ">
          <Link to="/">
            <a className="uk-button uk-icon">Home </a>
          </Link>
        </ul>
      </nav>
    </>
  );
};

export default HomeButton;
