import ReactDOM from 'react-dom';
import React, { useState, useEffect } from 'react';
import { Tabs, Tab, TabTitleText, Checkbox } from '@patternfly/react-core';

import VersionLinks from './VersionLinks';
import PerformanceResults from './PerformanceResults';

class PlatformTabs extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      activeTabKey: 0
    };
    // Toggle currently active tab
    this.handleTabClick = (event, tabIndex) => {
      this.setState({
        activeTabKey: tabIndex
      });
    };
  }

  render() {
    const { activeTabKey } = this.state;
    const data = this.props.data;
    return (
      <div>
      <Tabs activeKey={activeTabKey} onSelect={this.handleTabClick}>
      {this.props.data.map((tab, index) => (         
        <Tab eventKey={index} title={<TabTitleText>{tab.title}</TabTitleText>}> 
          <VersionLinks data={tab.data} />
          <PerformanceResults data={tab.data} />
         </Tab>
       ))
      }
      </Tabs>
      </div>
    );
  }
}
export default PlatformTabs;