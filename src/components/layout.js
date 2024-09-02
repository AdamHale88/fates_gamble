import { Outlet } from "react-router-dom";
import Header from "./header";
import Footer from "./footer";

const Layout = () => {
    return (
      <div className="uk-margin-remove">
        <header
          className="uk-flex uk-flex-row uk-justify-content-center uk-margin-remove uk-align-center"
          uk-sticky="top"
        >
          <Header />
        </header>
        <main>          
          <Outlet />
        </main>
        <footer>
          <Footer />
        </footer>
      </div>
    );
};

export default Layout;

